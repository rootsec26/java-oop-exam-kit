# Instance Method مينفعش تعمل Override لـ Static
`A.m` static و`B.m` instance بنفس الـ signature — ده مش override قانوني، javac بيرفض: "overridden method is static". لازم static يقابل static وinstance يقابل instance.
