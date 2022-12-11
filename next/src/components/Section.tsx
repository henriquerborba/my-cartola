import { Paper, PaperProps } from "@mui/material";

export type SectioProps = PaperProps;

const Section = (props: SectioProps) => {
    return (
        <Paper
            {...props}
            variant="outlined"
            sx={{ padding: (theme) => theme.spacing(2), ...props.sx }}
        />
    );
};

export default Section;
