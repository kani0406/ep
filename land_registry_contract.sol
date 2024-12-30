// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract LandRegistry {
    struct Property {
        uint256 id;
        address owner;
        string location;
        uint256 size;
        uint256 value;
    }

    mapping(uint256 => Property) public properties;
    uint256 public propertyCount;

    function registerProperty(string memory _location, uint256 _size, uint256 _value) public {
        propertyCount++;
        properties[propertyCount] = Property(propertyCount, msg.sender, _location, _size, _value);
    }

    function transferProperty(uint256 _propertyId, address _newOwner) public {
        require(properties[_propertyId].owner == msg.sender, "Only the owner can transfer the property.");
        properties[_propertyId].owner = _newOwner;
    }

    function getPropertyOwner(uint256 _propertyId) public view returns (address) {
        return properties[_propertyId].owner;
    }
}
