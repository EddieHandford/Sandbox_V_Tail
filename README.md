# Sandbox_V_Tail

## Brief

An Open Source RC Glider designed to be a "sandbox" platform for people to experiment with, contribute to or to simply enjoy and share.

## Scope

This project is to provide a "Sandbox" Model Aeroplane platform that people can get involved with, creating multiple avenues of engagement/challenges/opportunities.

Some people may want to contribute mechanically to the design. For example, developing a new nose cone; another person may want to develop software for the BBC Micro:bit or develop a custom PCB! Or some people may just want to download the files and make their own kit!

There's no right or wrong; it's purely a project that allows for multiple disciplines of engineering to meet and develop something beneficial for the community.

The platform should always be designed with ease of use as priority, as the goal is to get as many people as possible excited about engineering and the world of flight. Clear documentation is key. For example, the current fuselage is an aluminium tube; although a carbon fibre tube is mechanically better, it is significantly more expensive. In order to make the project as accessible as possible, keeping the cost down is more important than marginal performance gains. This isn't a glider designed for breaking world records; it's designed to be a first glider or a development platform.

## Project Goals/Milestones

- **Goal 1:** Design, Manufacture and Test Fly a free flight glider
- **Goal 2:** Make the glider remote controlled (2 channel only)
- **Goal 2.5:** Produce a purchaseable kit form of the model with build instructions
- **Goal 3:** Add a BBC Micro:Bit to control the V Tail and produce software with basic functionality which works either standalone or in conjunction with an RX (such as compass hold)
- **Goal 4:** Add a winch launch hook for bungee launch
- **Goal 5:** Add a motor pod for manual, powered flight (note: doesn't need to be limited to electric, it could be piston engine)

## Design Snapshot 26/10/25

<img width="1387" height="787" alt="image" src="https://github.com/user-attachments/assets/bf143e17-26b4-4dbd-b69c-109f1519987a" />

## Restrictions

### Power

The use of a motor must be limited to only manual control; the motor control must never be controlled by a flight controller.

**Rationale:** Adding a motor to a system with any form of onboard flight controller/compute is too close to other projects such as Ardupilot, and is too easy to result in fly-aways or misuse of the platform.

### Military Use

This Project must never be used for military applications, no iteration of it, no derivative of it, no excuses.
