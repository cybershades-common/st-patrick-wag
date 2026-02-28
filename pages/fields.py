from .blocks import *


common_blocks = [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
    ('TwoColumnBlock',TwoColumnBlock()),
    ('SliderGalleryBlock',SliderGalleryBlock()),
    ('ContentWithImageAlignmentOption',ContentWithImageAlignmentOption()),
    ('VideoBlock',VideoBlock()),
    ('GalleryBlock',GalleryBlock()),
    ('FullwidthImageBlock',FullwidthImageBlock()),
    ('ContentWithVideoAlignmentOption',ContentWithVideoAlignmentOption()),
    ('LeadTextWithButtonBlock',LeadTextWithButtonBlock()),
    ('FullwidthImagewithButtonBlock',FullwidthImagewithButtonBlock()),
    ('QuotewithAuthorBlock',QuotewithAuthorBlock()),
    ('FullWidthQuoteBlock',FullWidthQuoteBlock()),
    ('NextPreviousBlock',NextPreviousBlock()),
    ('ExploreMoreGridBlock',ExploreMoreGridBlock()),
    ('CardGridwithTitleBlock',CardGridwithTitleBlock()),
    ('CardGridwithTitleandTextBlock',CardGridwithTitleandTextBlock()),
    ('QuickLinksGridBlock',QuickLinksGridBlock()),
    ('LatestNewsBlock',LatestNewsBlock()),
    ('LatestBlogBlock',LatestBlogBlock()),
    ('DynamicSnippetChooserBlock',DynamicSnippetChooserBlock()),
    ('StatisticsBlock',StatisticsBlock()),
    ('TestimonialsBlock',TestimonialsBlock()),
    ('CoCurricularSliderBlock',CoCurricularSliderBlock()),

]
homepage_stream_fields= common_blocks+ []


generalpage_stream_fields=common_blocks+[]
landingpage_stream_fields=common_blocks+[]
newspage_stream_fields = [
    ('VideoBlock',VideoBlock()),
    ('FullwidthImageBlock',FullwidthImageBlock()),
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
    ('TwoColumnBlock',TwoColumnBlock()),
]
content_holder_stream_fields= [
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('QuotewithAuthorBlock',QuotewithAuthorBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
]

blog_stream_fields = [
    ('VideoBlock',VideoBlock()),
    ('FullwidthImageBlock',FullwidthImageBlock()),
    ('HtmlSourceBlock',HtmlSourceBlock()),
    ('space',SpaceBlock()),
    ('ContentWithVariableWidthBlock',ContentWithVariableWidthBlock()),
    ('TwoColumnBlock',TwoColumnBlock()),
]