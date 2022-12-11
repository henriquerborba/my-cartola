import { Typography, TypographyProps } from "@mui/material";

export type LabelProps = TypographyProps;

const Label = (props: LabelProps) => {
    return (
        <Typography variant="h6" component={"span"} {...props}>
            {props.children}
        </Typography>
    );
};

export default Label;
