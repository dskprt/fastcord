import setuptools

setuptools.setup(name="fastcord",
    version="0.3.0",
    description="another discord api wrapper for writing bots",
    author="dskprt",
    url="https://github.com/dskprt/fastcord",
    packages=[ "fastcord", "fastcord.utils", "fastcord.objects" ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
    install_requires=[ "websocket-client" ],
    python_requires=">=3.6")
