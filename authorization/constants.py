PERMISSIONS = {
    # Patient
    "patient.create": {
        "name": "Create Patient",
        "description": "Allows the user to create a patient.",
    },
    "patient.read": {
        "name": "View Patient",
        "description": "Allows the user to view patient information.",
    },
    "patient.update": {
        "name": "Update Patient",
        "description": "Allows the user to update patient information.",
    },
    "patient.delete": {
        "name": "Delete Patient",
        "description": "Allows the user to delete a patient.",
    },

    # Appointment
    "appointment.create": {
        "name": "Create Appointment",
        "description": "Allows the user to create an appointment.",
    },
    "appointment.read": {
        "name": "View Appointment",
        "description": "Allows the user to view appointment information.",
    },
    "appointment.update": {
        "name": "Update Appointment",
        "description": "Allows the user to update an appointment.",
    },
    "appointment.delete": {
        "name": "Delete Appointment",
        "description": "Allows the user to delete an appointment.",
    },

    # Medical Record
    "medical_record.create": {
        "name": "Create Medical Record",
        "description": "Allows the user to create a medical record.",
    },
    "medical_record.read": {
        "name": "View Medical Record",
        "description": "Allows the user to view medical records.",
    },
    "medical_record.update": {
        "name": "Update Medical Record",
        "description": "Allows the user to update a medical record.",
    },
    "medical_record.delete": {
        "name": "Delete Medical Record",
        "description": "Allows the user to delete a medical record.",
    },
}

ROLES = {
    "admin": {
        "name": "Administrator",
        "description": "Full access to the healthcare platform.",
        "permissions": "*",
    },

    "doctor": {
        "name": "Doctor",
        "description": "Access to patient and medical record operations.",
        "permissions": [
            "patient.read",
            "patient.update",
            "appointment.read",
            "appointment.update",
            "medical_record.create",
            "medical_record.read",
            "medical_record.update",
        ],
    },

    "receptionist": {
        "name": "Receptionist",
        "description": "Access to patient registration and appointment operations.",
        "permissions": [
            "patient.create",
            "patient.read",
            "patient.update",
            "appointment.create",
            "appointment.read",
            "appointment.update",
        ],
    },

    "patient": {
        "name": "Patient",
        "description": "Access to the patient's own healthcare information.",
        "permissions": [
            "patient.read",
            "appointment.read",
            "medical_record.read",
        ],
    },
}