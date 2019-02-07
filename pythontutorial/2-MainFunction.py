print("Value of __name__",__name__)

def youCanCallMe():
    print('You can call me')
    print('This is the second statement')

print('This is the third statement')

def main():
    print ('This is from main function')
    youCanCallMe()

if(__name__=='__main__'):
    main()
print ('Another statement')


'''
# c

import <stdio.h>

int main()
{
	
}

# java


public class MyClass{
	
	public static void main(String args[])
	{

	}
}
'''