# bittu_subject = {"Physic", "Chemistry", "Computer Science", "Maths", "English"}
# shivam_subject = {"English", "Physic", "Computer Applicatio", "Chemistry", "Biology"}
# # print(f"{bittu_subject}\n{type(bittu_subject)}")
# # print(f"{shivam_subject}\n{type(shivam_subject)}")


# # ###common subject of Bittu & Shivam
# # #common_subject = bittu_subject.intersection(shivam_subject)         ## You can use as well as symboll of intersection
# # common_subject = bittu_subject & (shivam_subject)
# # print(common_subject)


# # ###All subject
# # #all_subject = bittu_subject.union(shivam_subject)         ## You can use as well as symboll of union
# # all_subject = bittu_subject | (shivam_subject)
# # print(all_subject)


# ### NOW ONE MORE THING ###
# piyush_subject = {"Hindi", "English", "Maths"}



# common_subject = bittu_subject & (shivam_subject) & piyush_subject
# print(common_subject)


# all_subject = bittu_subject | (shivam_subject) | piyush_subject
# print(all_subject)





days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
weekend = {"sat", "sun"}

### diffference of set
# weekdays = days.difference(weekend)   ##### You can use as well as symboll of difference
weekdays = days - weekend

print(weekdays)

