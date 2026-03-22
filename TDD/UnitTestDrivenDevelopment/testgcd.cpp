//testgcd.cpp写一个简单的测试代码testgcd.cpp
#include <gtest/gtest.h>
int Gcd(int a, int b)    //计算最大公约数
{
    return 0 == b ? a : Gcd(b, a % b); 
}
TEST(GcdTest, IntTest) //正确测试
{
    EXPECT_EQ(1, Gcd(2, 5));
    EXPECT_EQ(2, Gcd(2, 10));
    EXPECT_EQ(2, Gcd(2, 4));
    EXPECT_EQ(3, Gcd(6, 9));
}

TEST(GcdTest, IntTestWrongGcd) //错误测试-错误的最大公约数
{
    EXPECT_NE(9, Gcd(2, 5));
    EXPECT_NE(8, Gcd(2, 5));
    EXPECT_NE(1, Gcd(2, 4));
    EXPECT_NE(0, Gcd(6, 9));
}

TEST(GcdTest, IntTestBigFirst) //大数在前
{
    EXPECT_EQ(1, Gcd(5, 2));
    EXPECT_EQ(2, Gcd(64, 10));
    EXPECT_EQ(2, Gcd(4, 2));
    EXPECT_EQ(3, Gcd(30, 9));
}
int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
