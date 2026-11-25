# equals و hashCode بيخلو contains و remove يشتغلوا بالقيمة
مع `equals` و`hashCode` متعريفين على `x`، الـ `new P(1)` الجديدة بتساوي القديمة — `contains` بتلاقيها (true) و`remove` بتشيلها (true) فالقائمة بتفضل فاضية.
