from setuptools import setup

setup(
	name="media-dl",
	version="1.0.0",
	description="Universal Media Downloader for YouTube, SoundCloud and more.",
	author="Vincent",
	author_email="vbonnard.dev@gmail.com",
	py_modules=["media_dl"],
	install_requires=[
		"yt-dlp",
		"mutagen",
		"requests",
	],
	entry_points={
		'console_scripts': [
			'media-dl = media_dl:main',
		],
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)
