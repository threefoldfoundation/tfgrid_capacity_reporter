# Install zbundle(0-bundle)

Zbundle allows an flist to be run on any Linux system which can be used as a sandbox.
More information can be found in the [0-bundle repository](https://github.com/zero-os/0-bundle)

## Download precompiled binary

An autobuilded compiled version of zbundle can be found on: https://download.gig.tech/gig-autobuilder/

The latest build at moment of writing is: `zero-os-0-bundle-master-35e718b09f.tar.gz`

Click on it to download the file or copy the download url and use other tools to download it.

```sh
curl -o ~/Downloads/zbundle.tar.gz https://download.gig.tech/gig-autobuilder/zero-os-0-bundle-autobuild-f385a271dc.tar.gz
```

Unpack
```
mkdir ~/zbundle
tar xvf ~/Downloads/zbundle.tar.gz -C ~/zbundle
```

The executable can now be found at `~/zbundle/bin/zbundle`

Test zbundle command
```sh
~/zbundle/bin/zbundle --help

# or
cd ~/zbundle/bin
./zbundle --help
```

To make the zbundle command globally available
```sh
mv ~/zbundle/bin/zbundle /usr/local/bin/zbundle
```

Test zbundle command
```sh
zbundle --help
```
