# Turtlesim

dockerized environment for ROS tutorials

## Use

fork this repo and clone it to your local machine

navigate to the turtlesim directory

### building the image

run `.docker/build_image.sh` to build the docker image or `.docker/build_image_zsh.sh` to build the docker image if you are using zsh

### running the container

run `.docker/run_user.sh` to run the docker container or  `.docker/run_user_nvidia.sh` if you have an nvidia gpu and have installed the nvidia docker package

This will mount the users home directory to the container and run the container in interactive mode. You will not own the workspace run `sudo chown -R $USER /dev_ws` to take ownership of the workspace.

### terminal

#### multiple terminals

terminator is installed in the container and can be run with `terminator`.

#### sourcing the ROS environment

Add the following to your .bashrc (located in home/$USER) to automatically source the ROS environment when opening a new shell in the container.

```bash
if [ -f "/dev_ws/setup.bash" ]; then
    source /dev_ws/setup.bash
fi
```

or if you are using zsh to your .zshrc

```zsh
if [ -f "/dev_ws/setup.zsh" ]; then
    source /dev_ws/setup.zsh
fi
```

### vscode integration

requires the following vscode extensions to be installed

- [docker](https://code.visualstudio.com/docs/containers/overview)
- [remote development](https://code.visualstudio.com/docs/remote/remote-overview)

devcontainer.json is included in the .docker directory of this repo.

#### Attach vs code to container

In vs code go to the Docker tab in the side bar. Right click on the container named turtlesim:latest. Select attach vscode.

#### When attaching to the container for first time:

In vs code open the command palette (Ctrl-Shift-P).
Select Remote-containers: Open attached container configuration file.
Copy paste content of devcontainer.json and save.
Close the vscode window and reattach.
