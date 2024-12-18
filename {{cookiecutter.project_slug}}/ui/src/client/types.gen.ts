// This file is auto-generated by @hey-api/openapi-ts

export type HTTPValidationError = {
    detail?: Array<ValidationError>;
};

export type UserPublic = {
    id: (number | null);
    email: string;
    full_name: string;
    avatar_url: (string | null);
    is_active: boolean;
    created_at: string;
};

export type ValidationError = {
    loc: Array<(string | number)>;
    msg: string;
    type: string;
};

export type UsersGetUserProfileData = {
    headers?: {
        authorization?: (string | null);
    };
};

export type UsersGetUserProfileResponse = (UserPublic);

export type UsersGetUserProfileError = (HTTPValidationError);