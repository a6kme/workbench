// This file is auto-generated by @hey-api/openapi-ts

export const HTTPValidationErrorSchema = {
    properties: {
        detail: {
            items: {
                '$ref': '#/components/schemas/ValidationError'
            },
            type: 'array',
            title: 'Detail'
        }
    },
    type: 'object',
    title: 'HTTPValidationError'
} as const;

export const UserPublicSchema = {
    properties: {
        id: {
            anyOf: [
                {
                    type: 'integer'
                },
                {
                    type: 'null'
                }
            ],
            title: 'Id'
        },
        email: {
            type: 'string',
            title: 'Email'
        },
        full_name: {
            type: 'string',
            title: 'Full Name'
        },
        avatar_url: {
            anyOf: [
                {
                    type: 'string'
                },
                {
                    type: 'null'
                }
            ],
            title: 'Avatar Url'
        },
        is_active: {
            type: 'boolean',
            title: 'Is Active'
        },
        created_at: {
            type: 'string',
            format: 'date-time',
            title: 'Created At'
        }
    },
    type: 'object',
    required: ['id', 'email', 'full_name', 'avatar_url', 'is_active', 'created_at'],
    title: 'UserPublic'
} as const;

export const ValidationErrorSchema = {
    properties: {
        loc: {
            items: {
                anyOf: [
                    {
                        type: 'string'
                    },
                    {
                        type: 'integer'
                    }
                ]
            },
            type: 'array',
            title: 'Location'
        },
        msg: {
            type: 'string',
            title: 'Message'
        },
        type: {
            type: 'string',
            title: 'Error Type'
        }
    },
    type: 'object',
    required: ['loc', 'msg', 'type'],
    title: 'ValidationError'
} as const;