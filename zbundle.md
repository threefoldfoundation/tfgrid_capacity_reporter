# Install zbundle(0-bundle)

Zbundle allows an flist to be run on any Linux system which can be used as a sandbox.
More information can be found in the [0-bundle repository](https://github.com/zero-os/0-bundle)

## Download precompiled binary

An autobuilded compiled version of zbundle can be found on: https://download.gig.tech/zbundle

```sh
mkdir -p /opt/bin
wget -O /opt/bin/zbundle https://download.gig.tech/zbundle
cd /opt/bin
chmod +x zbundle
```

Test zbundle command
```sh
./zbundle --help
```

To make the zbundle command globally available
```sh
mv /opt/bin/zbundle /usr/local/bin/zbundle
```

Test zbundle command
```sh
zbundle --help
```
