package main.java;
/**
 * 在继承链中，我们将子类向父类转换称为“向上转型”，将父类向子类转换称为“向下转型”。
 * 注意：不能直接将父类的对象强制转换为子类类型，只能将向上转型后的子类对象再次转换为子类类型。也就是说，子类对象必须向上转型后，才能再向下转型。
 */
public class Instanceof {
	public static void main(String[] args) {
        // 引用 People 类的实例
        People superObj = new People();
        System.out.println("// 引用 People 类的实例：WhatInstanceOf(superObj);");
        WhatInstanceOf(superObj);
        // 引用 President 类的实例
        President sonObj = new President();
        System.out.println("// 引用 President 类的实例： WhatInstanceOf(sonObj);");
        WhatInstanceOf(sonObj);
        // 其他Object 类的示例
        final Object  i = null;
        System.out.println("// 其他Object 类的示例：Object i = null;");
        WhatInstanceOf(i);
        
        //下面的代码运行时会抛出异常，不能将父类对象直接转换为子类类型
        //President sonObj2 = (SonClass)superObj;
        
        //正确做法：先向上转型，再向下转型
        System.out.println("我们将子类向父类转换称为“向上转型”，将父类向子类转换称为“向下转型”。");
        superObj=sonObj;
        Teacher sonObj2=(Teacher)superObj;
        WhatInstanceOf(sonObj2);
        
	}
    public static void WhatInstanceOf(Object obj) {
        if(obj instanceof Object){
            System.out.println("我是一个对象");
        }
        if(obj instanceof People){
            System.out.println("我是人类");
        }
        if(obj instanceof Teacher){
            System.out.println("我是一名教师");
        }
        if(obj instanceof President){
            System.out.println("我是校长");
        }

        System.out.println("-----------");  

    }
}

class People{ }
class Teacher extends People{ }
class President extends Teacher{ }
