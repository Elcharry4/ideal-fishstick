from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from database.db_manager import DBManager
from models.task import Task
import threading
from kivy.clock import Clock
from datetime import datetime
from kivymd.app import MDApp

class EmployeeDetailsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_manager = DBManager()
        self.employee_id = None
        self.employee_name = ""
        self.tasks = []

    def update_employee_id(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.ids.toolbar.title = f"Actividades de {employee_name}"
        self.load_tasks()

    def load_tasks(self):
        self.show_loading()
        threading.Thread(target=self._load_tasks).start()

    def _load_tasks(self):
        self.tasks = self.db_manager.get_tasks_for_employee(self.employee_id)
        Clock.schedule_once(lambda dt: self.display_tasks(), 0)
        Clock.schedule_once(lambda dt: self.hide_loading(), 0)

    def display_tasks(self):
        self.ids.task_list.clear_widgets()
        if self.tasks:
            first_task = self.tasks[0]
            if first_task.priority == 1:
                task_item = OneLineAvatarIconListItem(text=first_task.name)
                check_icon = IconLeftWidget(icon="check")
                check_icon.bind(on_release=lambda widget: self.mark_task_completed(first_task))
                task_item.add_widget(check_icon)
                self.ids.task_list.add_widget(task_item)

            for task in self.tasks[1:]:
                task_item = OneLineAvatarIconListItem(text=task.name)
                task_item.add_widget(IconLeftWidget(icon="delete", on_release=lambda widget, t=task: self.delete_task(t)))
                task_item.add_widget(IconRightWidget(icon="arrow-down", on_release=lambda widget, t=task: self.move_task_down(t)))
                task_item.add_widget(IconRightWidget(icon="arrow-up", on_release=lambda widget, t=task: self.move_task_up(t)))
                if not task.name:
                    task_item.on_release = lambda t=task: self.select_activity_for_task(t)
                self.ids.task_list.add_widget(task_item)
        else:
            self.add_placeholder_task()

    def add_placeholder_task(self):
        task_item = OneLineAvatarIconListItem(text="Añadir actividad")
        task_item.on_release = lambda: self.select_activity_for_task(None)
        self.ids.task_list.add_widget(task_item)

    def add_task(self, employee_id, task_name, activity_type, quantity):
        new_task = Task(task_id=None, name=task_name, activity_type=activity_type, quantity=quantity, priority=self.db_manager.get_next_priority(employee_id))
        self.db_manager.add_task(employee_id, new_task)
        if new_task.priority == 1:
            self.db_manager.update_task_start_time(new_task.task_id, datetime.now())
        self.load_tasks()

    def select_activity_for_task(self, task):
        app = MDApp.get_running_app()
        activity_screen = app.manager.get_screen('activity_selection')
        activity_screen.set_employee(self.employee_id, self.employee_name)
        activity_screen.set_task(task)
        app.nav_controller.go_to_screen('activity_selection', 'left')

    def delete_task(self, task):
        self.db_manager.delete_task(task.task_id)
        self.db_manager.decrement_priorities(self.employee_id, task.priority)
        self.load_tasks()

    def move_task_up(self, task):
        idx = self.tasks.index(task)
        if idx > 1:  # No mover la tarea actual
            self.swap_tasks(idx, idx - 1)

    def move_task_down(self, task):
        idx = self.tasks.index(task)
        if idx < len(self.tasks) - 1:
            self.swap_tasks(idx, idx + 1)

    def swap_tasks(self, idx1, idx2):
        self.db_manager.swap_task_priorities(self.tasks[idx1].task_id, self.tasks[idx2].task_id)
        if self.tasks[idx2].priority == 1:
            self.db_manager.update_task_start_time(self.tasks[idx2].task_id, datetime.now())
        self.load_tasks()

    def mark_task_completed(self, task):
        self.db_manager.update_task_end_time(task.task_id, datetime.now())
        self.db_manager.complete_task(task.task_id, self.employee_id)
        # Check if the next task (priority 2) should start and update its start time
        if len(self.tasks) > 1:
            self.db_manager.update_task_start_time(self.tasks[1].task_id, datetime.now())
        self.load_tasks()

    def show_loading(self):
        self.ids.spinner.active = True

    def hide_loading(self):
        self.ids.spinner.active = False

    def go_back_to_orders(self):
        # Actualizar datos en la pantalla de órdenes
        app = MDApp.get_running_app()
        orders_screen = app.manager.get_screen('orders')
        
        # Actualizar los datos antes de navegar
        orders_screen.load_employees()

        # Navegar a la pantalla de órdenes
        app.nav_controller.go_to_screen('orders', 'right')