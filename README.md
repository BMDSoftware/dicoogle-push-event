# Dicoogle Push Event 

This is an example server to handle new events on Dicoogle, considering index-push-event Plugin.

## Installation

Run with poetry with the following instructions:
    
    
    poetry install
    poetry shell
    python -m flask --app src/main run -p 9005 --debug
    

# Example of configuration

This is an example of configurations for `Plugins/settings/z-index-push-event.xml`

```xml
<configuration>
    <callback>http://127.0.0.1:9005/notify_post</callback>
    <timeout>5</timeout>
    <modalities>
        <modality>
            <name>MR</name>
            <level>study</level>
        </modality>
    </modalities>
</configuration>

```

# Test

Send a few images, for instance using dicom-rs, to the Dicoogle. In this example, make sure you send MR images.

```bash
dicom-storescu DICOOGLE-STORAGE@localhost:6666 I_00002
```

After a few seconds, the server should receive the event and print the message. You can also check the logs on browser:
http://127.0.0.1:9005/
