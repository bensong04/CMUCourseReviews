category="Misc_Courses"
if test $1 = "CS"
then
    category="CS_Courses"
fi
if test $1 = "ECE"
then
    category="ECE_Courses"
fi
if test $1 = "Math"
then
    category="Math_Courses"
fi
filename="${category}/${2}.md"
touch $filename
cat secret/template.md > $filename
vim $filename
