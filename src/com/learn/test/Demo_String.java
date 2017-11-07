package com.learn.test;

import java.util.Scanner;

public class Demo_String {

	public static void main(String[] args) {
		/*
		 * 主程序
		 */
		Demo_String test = new Demo_String();
//		test.login();
		test.test();
		test.test2();
		test.test3();
		test.test4();
	}
	
	public void test() {
		/*
		 * 把字节数组转字符串
		 * String test = new String(数组,索引,数量)
		 *  sc.nextInt() 和sc.nextLine()一起使用的问题；只获取整数参数,因为程序nextInet遇到\r\n就会直接代表获取结束,
		 *  所以就会跳过直接运行到下面;
			解决方案：
				1.创建两次对象，缺点：浪费空间
				2.都用nextLine()方法
		 *
		 */
		int[] arr2 = {97, 98, 99};
		String aa = new String(arr2, 0, 3);
		System.out.println(aa);

		String s1 = new String("abc");		//记录的是堆内存对象的地址值;也是先建立“abc”在常量池的副本,也相当于建立了两个副本.
		String s2 = "abc";					//记录的是常量池的地址值
		System.out.println(s1 == s2);		//结果：false			//比较的是地址值
		System.out.println(s1.equals(s2));	//结果：true			//比较的是地址值位置的字符内容，区分大小写
		
		// 字符串API中的一些方法
		String test = "sdfsdfsdf";
		System.out.println(test.contains("s"));	//结果： true
		System.out.println(test.charAt(1));		//结果： d		//根据位置，找字符
		System.out.println(test.indexOf("s",4)); //结果： 6		//根据起始4位置，找s索引
		System.out.println(test.length());		//结果： 9
	}
	
	public void login() {
		/*
		 * 模拟登陆
		 */
		Scanner sc = new Scanner(System.in);
		for(int i = 0; i <= 3; i++) {
			System.out.println("请输入用户名：");
			String username = sc.nextLine();
			System.out.println("请输入密码：");
			String password = sc.nextLine();
			
			if("admin".equals(username) && "admin".equals(password) ) {
				System.out.println("welcome to Scanner System Platform !!!");
				break;
			}else {
				System.out.println("Type error !!!");
			}
		}
		System.out.println("Logout ... ");	
	}
	
	public void test2() {
		/*
		 * 字符串遍历
		 */
		String test = "wukongscanner";
		for(int i = 0; i < test.length(); i++) {
			char c = test.charAt(i);
			System.out.println(c);
		}
	}
	
	public void test3() {
		/*
		 * 统计不同类型字符个数
		 * 如：ABCDEFGabcdefg123456!@#$%^
		 * 分析：字符串是有字符组成的，而字符的值都是有范围的，痛殴范围来判断是否包含该字符
		 * 如果包含就让计数器变量自增
		 */
		String test = "ABCDEFGabcdefg123456!@#$%^";
		int big = 0;
		int small = 0;
		int num = 0;
		int other = 0;
		
		for(int i = 0 ; i < test.length(); i++) {
			char c = test.charAt(i);
			if(c >= 'A' && c <= 'Z') {
				big++;
			}else if(c >= 'a' && c <= 'z') {
				small++;
			}else if(c >= '0' && c <= '9') {	//字符0,c也是代表字符数字ascii
				num++;
			}else {
				other++;
			}
		}
		
		System.out.println(test + " 字符串中；包含大写字符出现次数: " + big + ";小写字符出现次数: " + small + ";数字字符出现"
				+ "次数: " + num + "；其它字符出现次数: " + other);
		
	}
	
	public void test4() {
		/*
		 * String转换功能
		 */
		String test = "abc";
		byte[] arr = test.getBytes();
		for(int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}
	

}
