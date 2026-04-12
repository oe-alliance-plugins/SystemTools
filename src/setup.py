from setuptools import setup
import setup_translate

pkg = 'Extensions.SystemTools'
setup(name='enigma2-plugin-extensions-systemtools',
       version='0.7',
       description='SystemTools for enigma2 stb',
       package_dir={pkg: 'SystemTools'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', 'maintainer.info', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
