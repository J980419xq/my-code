## 基本信息
面试官您好，我叫蒋先强，今年25岁，本科毕业于华中科技大学软件学院，现在就读于中国科学技术大学计算机学院研究生三年级，实验室的研究方向是云网络与sdn  
## 概括句
接下来，我将介绍下个人的一些基本信息
## 信息
我在本科阶段开始学习Java，因为学校要求每年暑期会有一个工程实践活动，参与过多个Java WEB后台系统的开发，主要使用的是Spring MVC + SpringBoot + Mybatis。
在研究生阶段，我也参与过实验室的一些开源项目和科研项目，我们之前同华为共同研发过一款数据中心虚拟网络仿真器，我主要参与了部分模块的开发以及提出了一些架构上的建议。
今年暑假，我在美团的餐饮SaaS技术部实习了3个月时间，在这期间，我主要从事后端开发工作，熟悉了团队项目的开发规范和线上问题的治理，也在多个需求迭代中学习了多种中间件的使用，包括MySQL、Redis、Kafka和ElasticSearch
我自己平时对计算机网络、操作系统、linux、以及云计算等领域感兴趣，也做过一些简单的探索和研究，主要使用的技术栈是Java+Spring全家桶。
## 总结
总体上我觉得我的基础还算是比较扎实，学习能力也还可以，这就是我的自我介绍，感谢。

M端负责把餐饮saas各业务研发的产品及服务（智能POS机、会员管理、点餐助手等）通过销售人员上单动作售卖交付给商家，负责整个产品的完整生命周期。

```
configuration:
  name: configuration-1
  id: ""
  network-config:
    name: network-config1
    id: ""
    number_of_vpcs: 3
    number_of_subnets_per_vpc: 3
    subnet_ciders:
      - 10.0.1.0/24
      - 10.0.2.0/24
    number_of_security_groups: 1
    routers:
      - name: router1
        id: ""
        subnet-gw:
          - 10.0.1.1
          - 10.0.2.1
    security_groups:
      - name: secgroup1
        id: ""
        rules:
          - name: rule1
            id: ""
            ethertype: ipv4
            direction: ingress
            protocol: tcp
            port_range:
              - any
        apply_to:
          - vmgroup1
          - vmgroup2

```