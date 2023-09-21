// PDF upload component

// Imports
import { React } from "react";
import { Document, Page, Text, View, StyleSheet } from "@react-pdf/renderer";

// StyleSheet
const documentStyles = StyleSheet.create(
    
    {
        // Page styling
        page: {
            flexDirection: "row",
            backgroundColor: "#E4E4E4"
        },

        // Section styling
        section: {
            margin: 10,
            padding: 10,
            flexGrow: 1
        }
    }
);

// Component 
const DocumentView = () => {
    <Document>
        <Page size = "A4" style = { documentStyles.page }>
            <View style = { documentStyles.section } >


            </View>
        </Page>
    </Document>
}

