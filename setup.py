from setuptools import setup

setup(
    name='media-dl',
    version='1.0',
    py_modules=['media_dl'],
    install_requires=['yt-dlp', 'mutagen', 'requests'],
    entry_points='''
        [console_scripts]
        media-dl=media_dl:main
    ''',
)