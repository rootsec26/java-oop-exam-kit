# overload resolution: int

الـ compiler بيختار أقرب نوع: `5` int بالظبط → int، `5L` long → long، `5.0f` float بيتحول double (مفيش long)، `5.0` double → double.
