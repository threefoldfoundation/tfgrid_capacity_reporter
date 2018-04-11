#! /usr/bin/python3
"Docker image build script for capacity report image"
from js9 import j


def _install_js(prefab, branch):
    """
    Install jumpscale on provided prefab
    """
    prefab.js9.js9core.install(branch=branch)
    for component in ("core9", "lib9", "prefab9"):
        cmd = "cd /opt/code/github/jumpscale/%s; ./install.sh" % component
        prefab.core.run(cmd)
    prefab.core.run("sed -i 's/filter = \\[\\]/filter = [\"*\"]/g' /root/js9host/cfg/jumpscale9.toml")
    prefab.core.run("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")

def _install_report_deps(prefab):
    """
    Install j.sal.ubuntu.capacity dependencies on provided prefab
    """
    prefab.system.package.install("dmidecode")
    prefab.monitoring.smartmontools.install()

def build_docker(jsbranch, push, image):
    """
    Build and push a docker capacity report image
    """
    print("Starting docker container ... ", end='')
    container = j.sal.docker.create(base="ubuntu:16.04", command="sleep 3600", ssh=False)
    container.start()
    print("done!\nEstablishing prefab connection ... ", end='')
    try:
        ex = j.tools.executor.getLocalDocker(container.id)
        prefab = j.tools.prefab.get(executor=ex)
        print("done!\nUpdating ubuntu apt definitions ... ", end='')
        prefab.system.package.mdupdate()
        print("done!\nInstalling python3-dev, git, curl & language-pack-en ... ", end='')
        prefab.system.package.install("python3-dev,git,curl,language-pack-en")
        print("done!\nInstalling jumpscale ... ", end='')
        _install_js(prefab, jsbranch)
        print("done!\nCommiting jumpscale docker image ... ", end='')
        container.commit("jumpscale/js9")
        _install_report_deps(prefab)
        print("done!\nCommiting %s docker image ... " % image, end='')
        container.commit(image)
    finally:
        container.destroy()
    if push:
        print("done!\nPushing docker image ... ")
        j.sal.docker.push(image)
        print("%s build and published successfully!" % image)
    else:
        print("done!\n%s build successfully!" % image)


def _main():
    import argparse
    parser = argparse.ArgumentParser("Build and push docker capacity report image")
    parser.add_argument("--jsbranch", type=str, default="development",
                        help="Jumpscale git branch, tag or revision to build")
    parser.add_argument("--push",  action='store_true', help="Push to docker hub")
    parser.add_argument("--image",  type=str, default="jumpscale/reportbuilder", help="Name (and tag) of the image to commit to")
    parser.add_argument("--debug", help="Print debug information")
    args = parser.parse_args()
    if not args.debug:
        j.logger.loggers_level_set('INFO')
    build_docker(args.jsbranch, args.push, args.image)


if __name__ == "__main__":
    _main()
