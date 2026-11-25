# byte = byte + int

`b + 5` نوعه int وint مش بيتحول لـ byte من غير cast. الحل: `b = (byte)(b + 5)` أو `b += 5` اللي بتعمل cast ضمني.
