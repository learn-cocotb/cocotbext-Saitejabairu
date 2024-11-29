
module gpib_dut (
   input wire clk,
    input wire rst_n,
    input wire [7:0] data_in, // Data to send to DUT
    input wire send_data, // Signal to start sending data
    output reg [7:0] data_out, // Data output from DUT
    output reg NRFD, // Not Ready For Data
    output reg NDAC, // Not Data Accepted
    output reg DAV, // Data Valid
    output reg ATN // Attention
);

// State definitions for simple FSM
typedef enum logic [1:0] {
    IDLE = 2'b00,
    ACTIVE = 2'b01,
    WAIT = 2'b10
} state_t;

state_t state, next_state;

// Sequential block for FSM
always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= IDLE;
        data_out <= 8'b0;
        NRFD <= 1;
        NDAC <= 1;
        DAV <= 0;
        ATN <= 0;
    end else begin
        state <= next_state;
        case (next_state)
            IDLE: begin
                data_out <= 8'b0;
                NRFD <= 1;
                NDAC <= 1;
                DAV <= 0;
                ATN <= 0;
            end
            ACTIVE: begin
                data_out <= data_in;
                NRFD <= 0;
                NDAC <= 0;
                DAV <= 1;
                ATN <= 0;
            end
            WAIT: begin
                NRFD <= 1;
                NDAC <= 1;
                DAV <= 0;
                ATN <= 0;
            end
        endcase
    end
end

// Next state logic
always_comb begin
    next_state = state;
    case (state)
        IDLE: begin
            if (send_data) begin
                next_state = ACTIVE;
            end
        end
        ACTIVE: begin
            next_state = WAIT;
        end
        WAIT: begin
            next_state = IDLE;
        end
    endcase
end
endmodule
