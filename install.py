try:
    from extensions.sd_dreambooth_extension.postinstall import actual_install
except:
    from postinstall import actual_install

actual_install()