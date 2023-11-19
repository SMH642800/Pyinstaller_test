# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_windowsOS.py'],
    pathex=[],
    binaries=[],
    datas=[('Babel_Tower_windowOS.ico', '.'), ('sub-google-api.html', '.'), ('css', 'css'), ('img', 'img')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
      'PySide6.QtNetwork', 
      'PySide6.QtSql', 
      'PySide6.QtDBus',
      'PySide6.QtOpenGL',
      'PySide6.QtPdf',
      'PySide6.QtQml',
      'PySide6.QtQmlModels',
      'PySide6.QtQuick',
      'PySide6.QtVirtualKeyboard'
    ],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Babel Tower',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='Babel_Tower_windowOS.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
