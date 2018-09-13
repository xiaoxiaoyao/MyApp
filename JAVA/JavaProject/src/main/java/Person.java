/**  
 * Project Name:JavaProject  
 * File Name:Person.java  
 * Package Name:main.java  
 * Date:2018年1月2日下午10:20:32  
 * Copyleft (c) 2018, git@github.com:xiaoxiaoyao/MyApp.git .
 *  
*/  
  
package main.java;

import java.util.Arrays;
import java.util.stream.Collectors;

/**  
 * ClassName:Person <br/>  
 * Function: jdk8新特性-亮瞎眼的lambda表达式. <br/>  
 * Reason:   jdk8之前，尤其是在写GUI程序的事件监听的时候，各种的匿名内部类，大把大把拖沓的代码，程序毫无美感可言！既然java中一切皆为对象，那么，就类似于某些动态语言一样，函数也可以当成是对象啊！代码块也可以当成是对象啊！随着函数式编程的概念越来越深入人心，java中CODE=OBJECT的这一天终于到来了！如果你认为lambda表达式仅仅是为了从语法上简化匿名内部类，那就太小看jdk8的lambda了！. <br/>  
 * Date:     2018年1月2日 下午10:20:32 <br/>  
 * @author   yao  
 * @version    
 * @since    JDK 1.6  
 * @see        http://blog.csdn.net/goldenfish1919/article/details/22747375
 */

public class Person{  
        public String firstName;  
        public String lastName;  
        public int age;  
        public Person(String firstName, String lastName, int age){  
                this.firstName = firstName;  
                this.lastName = lastName;  
                this.age = age;  
        }  
        public String getFirstName(){  
                return this.firstName;  
        }  
        public String getLastName(){  
                return this.lastName;  
        }  
        public int getAge(){  
                return this.age;  
        }  
        public String toString(){  
                return firstName+","+lastName+","+age;  
        }  
        public String toJson(){  
                return "{"+  
                                "firstName:\""+firstName+"\","+  
                                "lastName:\""+lastName+"\","+  
                                "age:"+age +  
                                "}";  
        }  
        public static void main(String args[]){  
         Person people[] = new Person[]{  
                 new Person("Ted", "Neward", 10),  
                 new Person("Charlotte", "Neward", 41),  
                 new Person("Michael", "Naward", 19),  
                 new Person("Matthew", "Nmward", 13)  
         };  
         // 来个牛逼的
         String json = Arrays.asList(people).stream().map(Person::toJson).collect(Collectors.joining(", ", "[", "]"));  
         System.out.println(json);  
 }  
}  