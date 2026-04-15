block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('invoice_template.docx', '.')],  # plantilla Word
    hiddenimports=[
        'customtkinter',
        'docxtpl',
        'docx'
    ],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='invoice-generator',
    debug=False,
    console=False,  # app gráfica
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='invoice-generator'
)
