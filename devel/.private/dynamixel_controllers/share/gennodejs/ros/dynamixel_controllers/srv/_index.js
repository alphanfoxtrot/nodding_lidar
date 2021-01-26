
"use strict";

let SetSpeed = require('./SetSpeed.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')
let StopController = require('./StopController.js')
let TorqueEnable = require('./TorqueEnable.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')
let RestartController = require('./RestartController.js')
let StartController = require('./StartController.js')
let SetTorqueLimit = require('./SetTorqueLimit.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')

module.exports = {
  SetSpeed: SetSpeed,
  SetComplianceMargin: SetComplianceMargin,
  StopController: StopController,
  TorqueEnable: TorqueEnable,
  SetComplianceSlope: SetComplianceSlope,
  RestartController: RestartController,
  StartController: StartController,
  SetTorqueLimit: SetTorqueLimit,
  SetCompliancePunch: SetCompliancePunch,
};
