from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file_image_media_metadata_location import FileImageMediaMetadataLocation





T = TypeVar("T", bound="FileImageMediaMetadata")



@_attrs_define
class FileImageMediaMetadata:
    """ Additional metadata about image media, if available.

        Attributes:
            aperture (float | Unset): The aperture used to create the photo (f-number).
            camera_make (str | Unset): The make of the camera used to create the photo.
            camera_model (str | Unset): The model of the camera used to create the photo.
            color_space (str | Unset): The color space of the photo.
            exposure_bias (float | Unset): The exposure bias of the photo (APEX value).
            exposure_mode (str | Unset): The exposure mode used to create the photo.
            exposure_time (float | Unset): The length of the exposure, in seconds.
            flash_used (bool | Unset): Whether a flash was used to create the photo.
            focal_length (float | Unset): The focal length used to create the photo, in millimeters.
            height (int | Unset): The height of the image in pixels.
            iso_speed (int | Unset): The ISO speed used to create the photo.
            lens (str | Unset): The lens used to create the photo.
            location (FileImageMediaMetadataLocation | Unset): Geographic location information stored in the image.
            max_aperture_value (float | Unset): The smallest f-number of the lens at the focal length used to create the
                photo (APEX value).
            metering_mode (str | Unset): The metering mode used to create the photo.
            rotation (int | Unset): The number of clockwise 90-degree rotations applied from the image's original
                orientation.
            sensor (str | Unset): The type of sensor used to create the photo.
            subject_distance (int | Unset): The distance to the subject of the photo, in meters.
            time (str | Unset): The date and time the photo was taken (EXIF DateTime).
            white_balance (str | Unset): The white balance mode used to create the photo.
            width (int | Unset): The width of the image in pixels.
     """

    aperture: float | Unset = UNSET
    camera_make: str | Unset = UNSET
    camera_model: str | Unset = UNSET
    color_space: str | Unset = UNSET
    exposure_bias: float | Unset = UNSET
    exposure_mode: str | Unset = UNSET
    exposure_time: float | Unset = UNSET
    flash_used: bool | Unset = UNSET
    focal_length: float | Unset = UNSET
    height: int | Unset = UNSET
    iso_speed: int | Unset = UNSET
    lens: str | Unset = UNSET
    location: FileImageMediaMetadataLocation | Unset = UNSET
    max_aperture_value: float | Unset = UNSET
    metering_mode: str | Unset = UNSET
    rotation: int | Unset = UNSET
    sensor: str | Unset = UNSET
    subject_distance: int | Unset = UNSET
    time: str | Unset = UNSET
    white_balance: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_image_media_metadata_location import FileImageMediaMetadataLocation
        aperture = self.aperture

        camera_make = self.camera_make

        camera_model = self.camera_model

        color_space = self.color_space

        exposure_bias = self.exposure_bias

        exposure_mode = self.exposure_mode

        exposure_time = self.exposure_time

        flash_used = self.flash_used

        focal_length = self.focal_length

        height = self.height

        iso_speed = self.iso_speed

        lens = self.lens

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        max_aperture_value = self.max_aperture_value

        metering_mode = self.metering_mode

        rotation = self.rotation

        sensor = self.sensor

        subject_distance = self.subject_distance

        time = self.time

        white_balance = self.white_balance

        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aperture is not UNSET:
            field_dict["aperture"] = aperture
        if camera_make is not UNSET:
            field_dict["cameraMake"] = camera_make
        if camera_model is not UNSET:
            field_dict["cameraModel"] = camera_model
        if color_space is not UNSET:
            field_dict["colorSpace"] = color_space
        if exposure_bias is not UNSET:
            field_dict["exposureBias"] = exposure_bias
        if exposure_mode is not UNSET:
            field_dict["exposureMode"] = exposure_mode
        if exposure_time is not UNSET:
            field_dict["exposureTime"] = exposure_time
        if flash_used is not UNSET:
            field_dict["flashUsed"] = flash_used
        if focal_length is not UNSET:
            field_dict["focalLength"] = focal_length
        if height is not UNSET:
            field_dict["height"] = height
        if iso_speed is not UNSET:
            field_dict["isoSpeed"] = iso_speed
        if lens is not UNSET:
            field_dict["lens"] = lens
        if location is not UNSET:
            field_dict["location"] = location
        if max_aperture_value is not UNSET:
            field_dict["maxApertureValue"] = max_aperture_value
        if metering_mode is not UNSET:
            field_dict["meteringMode"] = metering_mode
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if sensor is not UNSET:
            field_dict["sensor"] = sensor
        if subject_distance is not UNSET:
            field_dict["subjectDistance"] = subject_distance
        if time is not UNSET:
            field_dict["time"] = time
        if white_balance is not UNSET:
            field_dict["whiteBalance"] = white_balance
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_image_media_metadata_location import FileImageMediaMetadataLocation
        d = dict(src_dict)
        aperture = d.pop("aperture", UNSET)

        camera_make = d.pop("cameraMake", UNSET)

        camera_model = d.pop("cameraModel", UNSET)

        color_space = d.pop("colorSpace", UNSET)

        exposure_bias = d.pop("exposureBias", UNSET)

        exposure_mode = d.pop("exposureMode", UNSET)

        exposure_time = d.pop("exposureTime", UNSET)

        flash_used = d.pop("flashUsed", UNSET)

        focal_length = d.pop("focalLength", UNSET)

        height = d.pop("height", UNSET)

        iso_speed = d.pop("isoSpeed", UNSET)

        lens = d.pop("lens", UNSET)

        _location = d.pop("location", UNSET)
        location: FileImageMediaMetadataLocation | Unset
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = FileImageMediaMetadataLocation.from_dict(_location)




        max_aperture_value = d.pop("maxApertureValue", UNSET)

        metering_mode = d.pop("meteringMode", UNSET)

        rotation = d.pop("rotation", UNSET)

        sensor = d.pop("sensor", UNSET)

        subject_distance = d.pop("subjectDistance", UNSET)

        time = d.pop("time", UNSET)

        white_balance = d.pop("whiteBalance", UNSET)

        width = d.pop("width", UNSET)

        file_image_media_metadata = cls(
            aperture=aperture,
            camera_make=camera_make,
            camera_model=camera_model,
            color_space=color_space,
            exposure_bias=exposure_bias,
            exposure_mode=exposure_mode,
            exposure_time=exposure_time,
            flash_used=flash_used,
            focal_length=focal_length,
            height=height,
            iso_speed=iso_speed,
            lens=lens,
            location=location,
            max_aperture_value=max_aperture_value,
            metering_mode=metering_mode,
            rotation=rotation,
            sensor=sensor,
            subject_distance=subject_distance,
            time=time,
            white_balance=white_balance,
            width=width,
        )


        file_image_media_metadata.additional_properties = d
        return file_image_media_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
