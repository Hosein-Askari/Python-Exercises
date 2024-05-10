Classes :
    Time

Functions:

    sum() : summation

    sub() : subtraction.

    time_to_second()

    second_to_time()

    gmt_to_iran()

    fix()  

    show()

How to use?

For sum and sub you need  to create two objects .when you creat object first argument is hour and second one is minute and third one is seconds.
For result you need to creat another object and in the end you should use show() funcion. 

for example :

a=Time(4,5,45)
b=Time(14,9,55)
c=a.sum(b)
c.show()

tip 1-  when you use time_to_second  you just need to call , no need of creating new object.

for example :

a =Time(4,45,57)
a.time_to_second()

tip 2-  when you wanns use second_to_time  you must input first and second argument as zero while you creating object.

for example :

a =Time(0,0,3640)
a.second_to_time()
a.show()

tip 3- if you wanna use gmt_to_iran function . you need to creat anothe object for result.

for example : 

a=Time(4,5,45)
b=a.gmt_to_iran()
b.show()