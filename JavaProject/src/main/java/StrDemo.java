package main.java;

public class StrDemo {

	public static void main(String[] args) {
		String s = "abc";
		StringBuffer sb1 = new StringBuffer();  // 这样初始化出的StringBuffer对象是一个空的对象,16个字节长度的缓冲区
		//StringBuilder sbBuilder1 = new StringBuilder("This is only a StringBuilder");  // StringBuilder 字符串变量（非线程安全）
		
		//使用说明：
		//strBuf1=(StringBuffer)s;  // StringBuffer和String属于不同的类型，不存在继承关系，不能直接进行强制类型转换
		StringBuffer sb2 = new StringBuffer(s);  // String转换为StringBuffer
		System.out.println("String转换为StringBuffer需要通过new StringBuffer()实现，String："+s+"  StringBuffer："+sb2.toString());
		s=sb1.toString();  // StringBuffer转换为String
		sb1.append(s);  // 这样append修改是可以的
		
		//StringBuffer类中的方法主要偏重于对于字符串的变化，例如追加、插入和删除等
		main.java.StrDemo.stringVsStringBuffer(s, sb1);		
		System.out.println("//注意StringBuffer被修改后可以返回 StringBuffer: " + sb1.toString());
	}
	/**
	 * 为什么用append插入呢？因为效率高啊。以下用String和StringBuffer分别拼装SQL语句1000次
	 * @param s,sb1
	 */
	public static void stringVsStringBuffer(String s,StringBuffer sb1){
		final int times = 100000;
        // 通过String对象
        long timeStart1 = System.currentTimeMillis();
        String sInfo[] = {"SELECT * FROM INFO WHERE INFO=","UESRNAME",";"};
        for (int i=0; i<times; i++) {
            s=sInfo[0]+sInfo[1]+sInfo[2];
        }
        long timeEnd1 = System.currentTimeMillis();
        System.out.println("String: " + s + "消耗时间"+(timeEnd1 - timeStart1) + "ms");
        // 通过StringBuffer对象
        timeStart1 = System.currentTimeMillis();
        for (int i=0; i<times; i++) {
        	sb1.setLength(0);
            sb1.append("select * from userInfo where username=")
            .append(sInfo[1])
            .append(";");
        }
        timeEnd1 = System.currentTimeMillis();
        System.out.println("StringBuffer: " + sb1.toString() +  "消耗时间"+(timeEnd1 - timeStart1) + "ms");	
	}

}
