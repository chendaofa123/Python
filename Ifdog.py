# -*- coding: cp936 -*-
age = int(input("��������ҹ���������: "))
print("")
if age < 0:
    print("�����ڶ��Ұ�!")
elif age == 1:
    print("�൱�� 14 ����ˡ�")
elif age == 2:
    print("�൱�� 22 ����ˡ�")
elif age > 2:
    human = 22 + (age -2)*5
    print("��Ӧ��������: ", human)
