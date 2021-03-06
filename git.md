# git
![alt git图解](git-3.png)
![alt git图解](git-1.png)
> + **Workspace 工作区**
> + **Index / Stage 暂存区**
> + **Repository 仓库区(本地仓库)**
> + **Remote 远程仓库**

    git add .
    git commit -m 'message'
    git push -u origin master # -u参数指定一个默认主机

## 查看分支
- git branch 查看本地分支
- git branch -a 查看所有分支（本地与远程）
- git branch -r 查看远程分支
- git branch -vv 查看本地分支与远程分支之间的关联关系

![alt git图解2](git-2.png)

## ssh agent详解 
[详细地址](https://www.thisfaner.com/p/ssh-agent/)
> ssh agent是一个密钥管理器，用来管理一个多个密钥，并为其他需要使用 ssh key 的程序提供代理。

- **添加密钥ssh-add**
>运行 ssh-add 时， 如果提示 “Could not open a connection to your authentication agent.” 说明你的ssh-agent并没有运行；使用下面的命令运行 ssh agent，再使用ssh-add命令添加你的 ssh key。

>ssh-add 这个命令不是用来永久性的记住你所使用的私钥的。实际上，它的作用只是把你指定的私钥添加到 ssh-agent 所管理的一个 session 当中。而 ssh-agent 是一个用于存储私钥的临时性的 session 服务，也就是说当你重启之后，ssh-agent 服务也就重置了。
> windows每次都要启动ssh-add后才能免密上传

` shell `

    # 先启动，再运行
    # macOS/Linux
    $ eval `ssh-agent`
    ssh-add ~/.ssh/other_id_rsa

    # 在Windows中的git-bash中
    $ eval $(ssh-agent)
    ssh-add ~/.ssh/other_id_rsa

