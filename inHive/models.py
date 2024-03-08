from django.db import models

# Create a model for User(member)
class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password =  models.CharField(max_length=128)

    def __str__(self):
        return self.username


# Create a model for QueenBee(admin)
# class QueenBee(models.Model):
#     username = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password =  models.CharField(max_length=128)

#     def __str__(self):
#         return self.username


# Create a model for Hive(Project)
class Hive(models.Model):
    id = models.AutoField(primary_key=True)
    hiveTitle = models.CharField(max_length=100)
    hiveDescription = models.TextField()
    intendedUsers = models.IntegerField()
    hiveStartDate = models.DateField()
    hiveEndDate = models.DateField()
    statusChoices = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived')
    ]
    status = models.CharField(max_length=20, choices=statusChoices)

    # queenBee = models.ForeignKey(QueenBee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + str(self.hiveTitle)


# Create a model for Task(assigned)
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    taskStartDate = models.DateField()
    taskEndDate = models.DateField()
    assignedTo = models.ForeignKey('User', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + " " + str(self.taskTitle)


# Create a model for Membership(members)
class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    roleChoices = [
        ('Member', 'Member'),
        ('QueenBee', 'QueenBee'),
        ('Soldier', 'Soldier')
    ]
    role = models.CharField(max_length=20, choices=roleChoices)

    def __str__(self):
        return "{} - {} ({})".format(str(self.User.id), str(self.hive), str(self.role))



