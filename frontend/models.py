from django.db import models

# Create your models here.
"""class report_details (models.Models):
    project_title = models.CharField(max_length=1000)
    proponent_name = models.CharField(max_length=1000)
    consultant_name = models.CharField(max_length=1000)
    project_location = models.CharField(max_length=1000)
    project_sector = models.CharField(max_lenght=1000)
    submission_date = models.DateField
    upload_time = models.DateTimeField"""


class management():
    name = str
    job_title = str
    description = str


class userdata(models.Model):
    Name_of_party = models.CharField(max_length=50)
    Industry = models.TextField(max_length=50)
    # Input=models.FloatField(default='This is mercury fed into the system, e.g an industrial sector')
    Activity_rate = models.FloatField(default='mercury inputs from the amount'
                                              ' of mercury containing material fed into the system')
    Input_factor = models.FloatField(default='general data on the mercury '
                                             'concentration in the feed material')
    Output_distribution_factors = models.FloatField(default='mercury amount '
                                                            'on the relevant release pathways based on available data')
    # Estimated_mercury_release_to_path_way_Y=
    Date_on_which_its_instrument_of_ratification = models.DateTimeField(
        auto_now_add=False)
    Location = models.TextField(max_length=50)

    def __str__(self):
        return self.Industry
