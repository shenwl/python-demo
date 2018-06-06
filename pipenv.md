## pipenv基础使用[创建的虚拟环境与项目绑定]

- 安装pipenv
```
pip install pipenv
```

- 创建虚拟环境
```
cd projectDir
pipenv install
```

- 进入虚拟环境
```
pipenv shell //未安装虚拟环境会自动安装
```

- 开始使用(安装包)
```
pipenv install flask
```

- 常用命令
```
// 退出虚拟环境
exit 

// 卸载包
pipenv uninstall flask

// 查看包的依赖关系
pipenv graph
```

- pipenv文档: https://github.com/pypa/pipenv
