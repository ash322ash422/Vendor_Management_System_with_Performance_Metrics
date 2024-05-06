from django.dispatch import Signal, receiver
from .models import HistoricalPerformance
from  .my_utils import dbg

# Define signals for calculating vendor performance metrics based changes in
# purchase order status.
po_acknowledged_signal = Signal()
po_status_completed_signal = Signal()


@receiver(signal = po_acknowledged_signal)
def update_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.average_response_time = vendor.calc_avg_response_time()
    vendor.save()
    
    return vendor


@receiver(signal = po_status_completed_signal)
def update_perfomance_metrics(sender, instance, **kwargs):
    vendor = instance.vendor
    #dbg("..inside update_perfomance_metrics")
    
    #compute metrics
    on_time_delivery_rate = vendor.calc_on_time_delivery_rate()
    quality_rating_avg = vendor.calc_avg_quality_ratings()
    fulfillment_rate = vendor.calc_fulfillment_rate()

    # dbg("..before:on_time_delivery_rate=",vendor.on_time_delivery_rate,
    #     ";quality_rating_avg=",vendor.quality_rating_avg,
    #     ";fulfillment_rate",vendor.fulfillment_rate)
   
    #update vendor metrics
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
    vendor.refresh_from_db()
    
    # dbg("..after:on_time_delivery_rate=",vendor.on_time_delivery_rate,
    #     ";quality_rating_avg=",vendor.quality_rating_avg,
    #     ";fulfillment_rate",vendor.fulfillment_rate)

    # create historical performance
    historical_performance_model = HistoricalPerformance
    historical_performance_model.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        fulfillment_rate=fulfillment_rate,
        average_response_time=vendor.average_response_time,
    )
    return vendor
