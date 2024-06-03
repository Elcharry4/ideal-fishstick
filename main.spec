# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2'],
    binaries=[],
    datas=[
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\config.ini', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\sources\\logopng2.png', 'sources'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\sources\\Poppins-SemiBold.ttf', 'sources'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\pre-splash.kv', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\login.kv', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\home.kv', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\config.kv', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\empleados.kv', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\kivy_files\\orders_screen.kv', 'kivy_files'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\kivy_files\\employee_details_screen.kv', 'kivy_files'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\kivy_files\\activity_selection_screen.kv', 'kivy_files'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\database\\db_manager.py', 'database'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\database\\config.ini', 'database'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\models\\employee_activity.py', 'models'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\models\\employee.py', 'models'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\models\\task.py', 'models'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\screens\\activity_selection_screen.py', 'screens'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\screens\\employee_details_screen.py', 'screens'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\screens\\orders_screen.py', 'screens'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\config.py', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\db.py', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\empleados.py', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\home.py', '.'),
        ('C:\\Users\\lisan\\OneDrive\\Documentos\\Python proyects\\Fundicion\\App\\app_2\\login.py', '.')
    ],
    hiddenimports=[
        'kivymd',
        'mysql.connector',
        'kivymd.uix.button',
        'kivymd.uix.label',
        'kivymd.uix.textfield',
        'kivymd.uix.datatables',
        'kivymd.uix.menu',
        'kivymd.uix.dialog',
        'kivymd.uix.relativelayout',
        'kivymd.uix.list',
        'kivymd.uix.responsivelayout',
        'kivymd.uix.floatlayout',
        'kivymd.uix.tab',
        'kivymd.toast',
        'kivymd.uix.dropdownitem',
        'kivymd.uix.selectioncontrol',
        'kivymd.uix.spinner',
        'kivymd.uix.behaviors',
        'kivymd.uix.navigationdrawer',
        'kivy.core.text',
        'kivy.graphics.stencil_instructions',
        'kivy.graphics.scissor_instructions',
        'kivy.graphics.vertex_instructions',
        'kivy.graphics.context_instructions',
        'kivy.graphics.fbo',
        'kivy.graphics.instructions',
        'kivy.graphics.texture',
        'kivy.graphics.vbo',
        'kivy.lib.gstplayer',
        'PIL._imaging',
        'PIL._imagingtk',
        'kivymd.uix.screenmanager',
        'PIL._imagingft',
        'PIL._imagingcms',
        'PIL._webp',
        'configparser',
        'datetime',
        'os',
        'threading',
        're'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,  # Añadir esto
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
