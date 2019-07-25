
很多技术细节已经通过ss工具架验证过了。基本上可行。以工具架作为轻量级探索，将成功经验用在浏览器上
接下来要面对的一个问题是路径化的问题
希望是这样的
pipe://192.168.50.39/projectName/!rootType="asset"/?cata="Charactor"/?step="Model"/?name="girl"/?varient="default"/?pubType="Main"

pipe://192.168.50.39/projectName/!rootType="shot"/?cata="seq000"/?step="LayoutAni"/?name="shot0010"/?varient="default"/?pubType="Main"


pipe://192.168.50.39/projectName/!rootType="cache"/?cata="seq000"/?step="FianalSceneAseemble"/?name="shot0010"/?varient="default"/?pubType="Main"


pipe://192.168.50.39/projectName/!rootType="preview"/?cata="seq000"/?step="Lighting"/?name="shot0010"/?varient="default"/?pubType="Main"

所有？开头的都是可选变量。
所有！开头的都是必填变量。

或许我需要一个数据库？但是这样的话就做不到开箱即用了。

尝试用docker配置一个数据库吧。如果整个系统的服务端都能在docker上就更妙了。

以目前的情况来看。可以使用Django构建一个页面系统。使用socket接入到maya中。

这个作为构想。

第一阶段，完成asset阶段的功能。
Model,Lookdev,Rig

注意版本的问题，命名-拓扑名-材质名。需要将这三个元素考虑进去。

拓扑名：经常作为变体使用。是否使用新的拓扑名。就在于这个角色的整体拓扑有没有改变，比如破洞，换衣服等。都算拓扑变化。

材质名：通常不会做太多变化，一般都只有dirt或者wet两个版本。在群集角色上会有很大的用处。用来给群众换色用的。



