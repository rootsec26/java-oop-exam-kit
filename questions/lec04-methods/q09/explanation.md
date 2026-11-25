# max(2.5, 3) مع max(int,int) بس

`2.5` double مش بيتحول لـ int — narrowing مش بيحصل أوتوماتيك في الـ method arguments. لازم `max(double,double)` overload أو cast.
