# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from shuup.front.views.checkout import SinglePageCheckoutView

urlpatterns = [
    url(r'^checkout/$', SinglePageCheckoutView.as_view(), name='checkout'),
    url(r'^checkout/(?P<phase>.+)/$', SinglePageCheckoutView.as_view(), name='checkout'),
    path('admin/', admin.site.urls),
    url(r'^sa/', include('shuup.admin.urls', namespace="shuup_admin")),
    url(r'^', include('shuup.front.urls', namespace="shuup")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
