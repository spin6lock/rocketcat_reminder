简介：

这是一个简单的例子，用来说明rocketchat的机器人如何主动push信息，默认有rocket.cat，不过需要手动改密码。auth token可以用curl获取：

```shell
curl https://your_domain_name/api/v1/login -d "username=rocket.cat&password=your_password"|jq ".data.authToken"
```
