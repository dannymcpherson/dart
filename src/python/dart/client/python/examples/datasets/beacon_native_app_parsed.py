from dart.client.python.dart_client import Dart
from dart.model.dataset import Column, DatasetData, Dataset, DataFormat, FileFormat, DataType, Compression, RowFormat, \
    LoadType

if __name__ == '__main__':
    dart = Dart('localhost', 5000)
    assert isinstance(dart, Dart)

    dataset = dart.save_dataset(Dataset(data=(DatasetData(
        name='beacon_native_app_parsed_v01',
        table_name='beacon_native_app',
        location='s3://example-bucket/nb.retailmenot.com/parsed_logs',
        load_type=LoadType.INSERT,
        data_format=DataFormat(
            FileFormat.TEXTFILE,
            RowFormat.DELIMITED,
            delimited_by='\t',
            quoted_by='"',
            escaped_by='\\',
            null_string='NULL',
            num_header_rows=1
        ),
        compression=Compression.NONE,
        partitions=[
            Column('year', DataType.STRING),
            Column('week', DataType.STRING),
        ],
        columns=[
            Column('logFileId', DataType.BIGINT),
            Column('lineNumber', DataType.INT),
            Column('created', DataType.TIMESTAMP, date_pattern="yyyy-MM-dd HH:mm:ss"),
            Column('remoteip', DataType.STRING),
            Column('useragent', DataType.STRING),
            Column('eventType', DataType.STRING),
            Column('appVersion', DataType.STRING),
            Column('advertiserID', DataType.STRING),
            Column('couponsOnPage', DataType.INT),
            Column('coupons', DataType.STRING),
            Column('channel', DataType.STRING),
            Column('geoCouponCount', DataType.STRING),
            Column('geofence', DataType.STRING),
            Column('geofenceTimeSpent', DataType.STRING),
            Column('loginStatus', DataType.STRING),
            Column('products', DataType.STRING),
            Column('session', DataType.STRING),
            Column('systemName', DataType.STRING),
            Column('systemVersion', DataType.STRING),
            Column('udid', DataType.STRING),
            Column('userQualifier', DataType.STRING),
            Column('url', DataType.STRING),
            Column('user_uuid', DataType.STRING),
            Column('userId', DataType.STRING),
            Column('searchType', DataType.STRING),
            Column('searchListTerm', DataType.STRING),
            Column('searchTerm', DataType.STRING),
            Column('emailUUId', DataType.STRING),
            Column('userFingerprint', DataType.STRING),
            Column('locationStatus', DataType.STRING),
            Column('pushNotificationStatus', DataType.BOOLEAN),
            Column('placement', DataType.STRING),
            Column('loc', DataType.STRING),
            Column('ppoi0', DataType.STRING),
            Column('ppoi1', DataType.STRING),
            Column('ppoi2', DataType.STRING),
            Column('ppoi3', DataType.STRING),
            Column('ppoi4', DataType.STRING),
            Column('appLaunchNotificationType', DataType.STRING),
            Column('scenarioName', DataType.STRING),
            Column('behaviorName', DataType.STRING),
            Column('couponType', DataType.STRING),
            Column('couponPosition', DataType.STRING),
            Column('hasQSRContent', DataType.BOOLEAN),
            Column('promptName', DataType.STRING),
            Column('locationPermissionChanage', DataType.STRING),
            Column('couponProblemType', DataType.STRING),
            Column('storeTitle', DataType.STRING),
            Column('mallName', DataType.STRING),
            Column('restaurantName', DataType.STRING),
            Column('milesAway', 'float'),
            Column('menuItem', DataType.STRING),
            Column('toolName', DataType.STRING),
            Column('toolAction', DataType.STRING),
            Column('toolStep', DataType.STRING),
            Column('mallPosition', DataType.INT),
            Column('recommendStoreName', DataType.STRING),
            Column('recommendStorePosition', DataType.INT),
            Column('favoriteStoreName', DataType.STRING),
            Column('favoriteStoreAction', DataType.STRING),
            Column('favoriteStorePosition', DataType.INT),
            Column('favoriteSiteId', DataType.STRING),
            Column('receiverName', DataType.STRING),
            Column('outclickButtonPrompt', DataType.STRING),
            Column('dataSource', DataType.STRING),
            Column('searchResultCount', DataType.INT),
            Column('searchResultPosition', DataType.INT),
            Column('shareType', DataType.STRING),
            Column('daysUntilExpiration', DataType.INT),
            Column('fireDate', DataType.BIGINT),
            Column('settingsChangeValue', DataType.STRING),
            Column('settingsChangeType', DataType.STRING),
            Column('settingsChangeLocation', DataType.STRING),
            Column('clickAction', DataType.STRING),
            Column('tnt', DataType.STRING),
            Column('previousPage', DataType.STRING),
            Column('clickPage', DataType.STRING),
            Column('launchReason', DataType.STRING),
            Column('taplyticsData', DataType.STRING),
            Column('appCampaign', DataType.STRING),
            Column('accountMethod', DataType.STRING),
            Column('appState', DataType.STRING),
            Column('btStatus', DataType.BOOLEAN),
            Column('btBeaconId', DataType.STRING),
            Column('btBeaconFactoryId', DataType.STRING),
            Column('btBeaconName', DataType.STRING),
            Column('btTimeSpent', DataType.STRING),
            Column('purchaseId', DataType.STRING),
            Column('transactionId', DataType.STRING),
            Column('outclickLink', DataType.STRING),
            Column('outclickPage', DataType.STRING),
            Column('featuredCouponPosition', DataType.INT),
            Column('commentCount', DataType.INT),
            Column('mallCount', DataType.INT),
            Column('clickCount', DataType.INT),
            Column('merchantName', DataType.STRING),
            Column('merchantPosition', DataType.INT),
        ],
    ))))
    print 'created dataset: %s' % dataset.id