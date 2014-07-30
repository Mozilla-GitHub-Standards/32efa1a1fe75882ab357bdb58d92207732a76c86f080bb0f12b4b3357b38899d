from django.conf import settings
from django.db.models import signals


if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
    from django.utils.translation import ugettext_noop as _

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notices = (
            ("test_notification", _(u"Notification tested"),
                _(u"a notification was tested")),
            # ("badge_edited", _(u"Badge edited"),
            #     _(u"one of your badges has been edited")),
            # ("badge_awarded", _(u"Badge awarded"),
            #     _(u"one of your badges has been awarded to someone")),
            # ("award_received", _(u"Award received"),
            #     _(u"you have been awarded a badge")),
            # ("award_accepted", _(u"Badge award accepted"),
            #     _(u"someone has accepted an award for one of your badges")),
            # ("award_declined", _(u"Badge award declined"),
            #     _(u"someone has declined an award for one of your badges")),
            # TODO: Notification on progress?
            # ("nomination_submitted", _(u"Nomination submitted"),
            #     _(u"someone has submitted a nomination for one of your badges")),
            # ("nomination_approved", _(u"Nomination approved"),
            #     _(u"a nomination you submitted for an award has been approved")),
            # ("nomination_rejected", _(u"Nomination rejected"),
            #     _(u"a nomination you submitted for an award has been rejected")),
            # ("nomination_received", _(u"Nomination received"),
            #     _(u"a nomination to award you a badge was approved")),
            # ("nomination_accepted", _(u"Nomination accepted"),
            #     _(u"a nomination you submitted for an award has been accepted")),
        )
        for notice in notices:
            notification.create_notice_type(*notice)

    signals.post_syncdb.connect(create_notice_types, sender=notification)
