=====
Uhome
=====

Uhome is python wrapper for communication with Uponor Smatrix Wave PLUS Smart Home Gateway, R-167 aka U@home. The module uses units REST API for discovery of controllers and thermostats.

=====
Usage
=====

Package consists of Uhome module and can be used in following way::

    u = Uhome('ip_address_of_u@home_module')
    u.update()

The discovery of controllers and thermostats registered with the unit is run when the object is created. After that method ``update()`` should be called to update the keys with values.

You can also do a rediscovery of controlles and/or thermostats using methods ``init_controllers()``and ``init_thermostats()``. The rediscovery is not done when updating.

Currently module only reads values. Adding support for setting values is on TODO list.

============
List of keys
============

**MODULE KEYS**

Located in ``uhome_module_keys`` dict of your Uhome object.

* module_id
* cooling_available
* holiday_mode
* forced_eco_mode
* hc_mode
* hc_masterslave
* ts_sv_version
* holiday_setpoint
* average_temp_low
* low_temp_alarm_limit
* low_temp_alarm_hysteresis
* remote_access_alarm
* device_lost_alarm
* no_comm_controller1
* no_comm_controller2
* no_comm_controller3
* no_comm_controller4
* average_room_temperature
* controller_presence
* allow_hc_mode_change
* hc_master_type

**CONTROLLER KEYS**

Located in ``uhome_controller_keys`` dict of your UhomeController objects.

* output_module
* rh_deadzone
* controller_sv_version
* thermostat_presence
* supply_high_alarm
* supply_low_alarm
* average_room_temperature_NO
* measured_outdoor_temperature
* supply_temp
* dehumidifier_status
* outdoor_sensor_presence

**THERMOSTAT KEYS**

Located in ``uhome_thermostat_keys`` dict of your UhomeThermostat objects.

* eco_profile_active_cf
* dehumidifier_control_activation
* rh_control_activation
* eco_profile_number
* setpoint_write_enable
* cooling_allowed
* rh_setpoint
* min_setpoint
* max_setpoint
* min_floor_temp
* max_floor_temp
* room_setpoint
* eco_offset
* eco_profile_active
* home_away_mode_status
* room_in_demand
* rh_limit_reached
* floor_limit_status
* technical_alarm
* tamper_indication
* rf_alarm
* battery_alarm
* rh_sensor
* thermostat_type
* regulation_mode
* room_temperature
* room_temperature_ext
* rh_value
* ch_linked_to_th
* room_name
* utilization_factor_24h
* utilization_factor_7d
* reg_mode
* channel_average
* radiator_heating

===========================
Hardware compatibility list
===========================

The module has been testet with following hardware:

* X-165 (controller)
* M-160 (slave module)
* I-167 (panel)
* R-167 (U@home module)
* T-169 (thermostat)

If you test it with other units, please let me know or even better update the list above.

=============
Documentation
=============

TODO: Make documentation.