from datetime import datetime
from django.db.models.signals import pre_save,pre_delete
from .models import Box
from django.dispatch import receiver
from backend.settings import A1,V1,L1,L2
from django.db.models import Sum
from datetime import timedelta
from django.core.exceptions import ValidationError

@receiver(pre_save,sender=Box)
def box_conditions(sender,instance,user,**kwargs):     
    # Conditions to be fulfilled on each add/update/delete
    
    # Condition 1 
    # Average area of all added boxes should not exceed A1
    total_area=Box.objects.aggregate(Sum('area'))
    total_boxes=Box.objects.count()

    if instance.pk:
        # in case update called on a box
        curr_box_area=Box.objects.get(pk=instance.pk)
        total_area=total_area+instance.area-curr_box_area
    else:
        # new box added
        total_area+=instance.area
        total_boxes+=1

    average_area=(total_area)/(total_boxes)
    
    if average_area>A1:
        raise ValidationError(f"This box can't be added as total box area average can't be greater than {A1}")

    # Condition 2
    # Average volume of all boxes added by the current user shall not exceed V1
    total_volume=Box.objects.filter(creator=user).aggregate(Sum('volume'))
    total_boxes=Box.objects.filter(creator=user).count()

    if instance.pk:
        # in case update called on a box
        curr_box_volume=Box.objects.get(pk=instance.pk)
        total_volume=total_volume+instance.volume-curr_box_volume
    else:
        # new box added
        total_volume+=instance.volume
        total_boxes+=1

    average_volume=(total_volume)/(total_boxes)
    
    if average_volume>V1:
        raise ValidationError(f"This box can't be added as total box volume average can't be greater than {V1}")

    # Condition 3
    # Total Boxes added in a week cannot be more than L1

    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    boxed_added_this_week=Box.objects.filter(created_on__range=[start_of_week,end_of_week]).count()

    if instance.pk is None and boxed_added_this_week >=L1:
        raise ValidationError(f"Total boxes added this week has reached limit - {L1}")
    
    # Condition 4
    # Total Boxes added in a week by a user cannot be more than L2

    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    boxed_added_this_week=Box.objects.filter(creator=user,created_on__range=[start_of_week,end_of_week]).count()

    if instance.pk is None  and boxed_added_this_week >=L2:
        raise ValidationError(f"Total boxes added this week by current user has reached limit - {L2}")
    
@receiver(pre_delete,sender=Box)
def box_conditions(sender,instance,user,**kwargs):     
    # Conditions to be fulfilled on each add/update/delete
    
    # Condition 1 
    # Average area of all added boxes should not exceed A1
    total_area=Box.objects.aggregate(Sum('area'))
    total_boxes=Box.objects.count()
    item_area=instance.area
    
    if total_boxes>1:
        average_area=(total_area-item_area)/(total_boxes-1)
        if average_area>A1:
            raise ValidationError(f"This box can't be added as total box area average can't be greater than {A1}")

    # Condition 2
    # Average volume of all boxes added by the current user shall not exceed V1
    total_volume=Box.objects.aggregate(Sum('volume'))
    total_boxes=Box.objects.count()
    item_volume=instance.volume
    if total_boxes>1:
        average_volume=(total_volume-item_volume)/(total_boxes-1) 
        if average_volume>V1:
            raise ValidationError(f"This box can't be added as total box volume average can't be greater than {V1}")
    
    # Condition 3 and condition not applicable in case of delete
    
